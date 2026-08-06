def read_job_description(file_path):
    """
    Read a job description text file and return its contents.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
