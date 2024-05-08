from google.cloud import storage


def upload_file_to_storage(local_file_path, bucket_name, blob_name):
  """
  This function uploads a local file to a Cloud Storage bucket.

  Args:
      local_file_path: Path to the file on your local machine.
      bucket_name: The name of the Cloud Storage bucket to upload the file to.
      blob_name: The desired name for the file within the bucket.

  Returns:
      None
  """

  # Create a Cloud Storage client
  client = storage.Client()

  # Upload the file
  blob = client.bucket(bucket_name).blob(blob_name)
  blob.upload_from_filename(local_file_path)

  print(f"File {local_file_path} uploaded successfully to bucket {bucket_name} as {blob_name}")


if __name__ == "__main__":
  local_file_path = "C:\\Users\\EBELENMGY\\Downloads\\students.csv"  # Replace with your file path
  bucket_name = "bucketdiprova1"  # Replace with your bucket name
  blob_name = "students"  # Replace with desired blob name

  upload_file_to_storage(local_file_path, bucket_name, blob_name)