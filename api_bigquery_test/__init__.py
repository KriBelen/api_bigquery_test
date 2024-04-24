"""
GCP Helper Scripts: BigQuery and Cloud Storage

This package contains reusable functions for interacting with GCP services:

* bigquery.py: Provides functions for querying BigQuery.
* storage.py: Provides functions for uploading files to Cloud Storage.

The if __name__ == "__main__":
block ensures that the code within that block only executes when the script is
run directly and not when imported as a module. This allows you to keep both
functionalities (BigQuery query and file upload) in separate files while still
being able to run them independently.
"""
