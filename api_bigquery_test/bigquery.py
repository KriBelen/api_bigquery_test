import logging
from google.cloud import bigquery


def run_bigquery_query(project_id, dataset_id, table_id):
  """
  This function establishes a BigQuery client, executes a query on a specified dataset and table,
  and returns the query results.

  Args:
      project_id: Your GCP project ID.
      dataset_id: The ID of the BigQuery dataset containing the table.
      table_id: The ID of the BigQuery table to query.

  Returns:
      A list of rows containing the query results.
  """

  # Configure logging
  logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

  # Set environment variable (optional, can be handled elsewhere)
  # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "..."

  # Create a BigQuery client
  client = bigquery.Client(project=project_id)

  logging.info(f"Using project: {project_id}, dataset: {dataset_id}, table: {table_id}")

  # Build the query
  query = f"SELECT * FROM `{dataset_id}`.`{table_id}`"

  # Execute the query
  rows = client.query(query).result()

  return rows


if __name__ == "__main__":
  project_id = "training-gcp-309207"
  dataset_id = "dataset_kristina"
  table_id = "example"

  # Run the function and get results
  results = run_bigquery_query(project_id, dataset_id, table_id)

  logging.info("Table retrieved and queried correctly")

  # Print the results
  for row in results:
    ID = row['ID']
    print("The result is: ID =", ID)