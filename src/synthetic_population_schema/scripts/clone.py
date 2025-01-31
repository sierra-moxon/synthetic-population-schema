from kghub_downloader.download_utils import download_from_yaml  # type: ignore
import os
from git import Repo
import pystow
import shutil
import subprocess
import zipfile
from concurrent.futures import ThreadPoolExecutor


def download_github_repo(repo_url, branch="main", output_dir="output"):
    """
    Clones a GitHub repository and extracts files from a specific branch.

    Args:
        repo_url (str): The URL of the GitHub repository to clone.
        branch (str): The branch to clone (default is 'main').
        output_dir (str): Directory where the repository will be cloned.
    """
    local_dir = pystow.join(output_dir)
    if os.path.exists(local_dir):
        print(f"Directory {local_dir} already exists. Removing for clean start.")
        shutil.rmtree(local_dir)

    print(f"Cloning {repo_url} into {local_dir}...")
    Repo.clone_from(repo_url, local_dir, branch=branch)
    print("Clone completed!")

    return local_dir


def is_already_extracted(extract_path):
    """
    Checks if any extracted files exist in the directory.
    """
    return os.path.exists(extract_path) and any(not fname.endswith(".zip") for fname in os.listdir(extract_path))


def download_and_extract(zip_url, output_path, extract_path):
    """
    Downloads and extracts a ZIP file if it has not already been extracted.
    """
    if is_already_extracted(extract_path):
        print(f"Skipping {zip_url}, already extracted.")
        return

    print(f"Downloading {zip_url} to {output_path}...")
    subprocess.run(["wget", "-O", output_path, zip_url], check=True)

    try:
        with zipfile.ZipFile(output_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Extracted {zip_url} in {extract_path}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_url} is not a valid ZIP file.")


def process_zip_files(base_url, category, dir_path):
    """
    Processes all ZIP files in a directory in parallel.
    """
    tasks = []
    with ThreadPoolExecutor() as executor:
        if category == "County":
            for state_code in os.listdir(dir_path):
                state_path = os.path.join(dir_path, state_code)
                if os.path.isdir(state_path):
                    for zip_file in os.listdir(state_path):
                        if zip_file.endswith(".zip"):
                            file_url = f"{base_url}/2010/{category}/{state_code}/{zip_file}"
                            output_path = os.path.join(state_path, zip_file)
                            tasks.append(executor.submit(download_and_extract, file_url, output_path, state_path))
        elif category == "State":
            for zip_file in os.listdir(dir_path):
                if zip_file.endswith(".zip"):
                    file_url = f"{base_url}/2010/{category}/{zip_file}"
                    output_path = os.path.join(dir_path, zip_file)
                    tasks.append(executor.submit(download_and_extract, file_url, output_path, dir_path))

        for task in tasks:
            task.result()


def download_files_with_wget(base_url, local_dir):
    """
    Downloads all .zip files from the constructed URLs using wget and extracts them in parallel.
    """
    for category in ["County", "State"]:
        dir_path = os.path.join(local_dir, "2010", category)

        if not os.path.exists(dir_path):
            print(f"Error: {category} directory {dir_path} does not exist!")
            continue

        process_zip_files(base_url, category, dir_path)

    print("All files downloaded and extracted successfully!")


if __name__ == "__main__":
    github_repo_url = "https://github.com/RTIInternational/SyntheticPopulations.git"
    base_download_url = "https://github.com/RTIInternational/SyntheticPopulations/raw/refs/heads/main"
    local_output_dir = "synthetic_populations"

    cloned_dir = download_github_repo(github_repo_url, branch="main", output_dir=local_output_dir)
    download_files_with_wget(base_download_url, cloned_dir)