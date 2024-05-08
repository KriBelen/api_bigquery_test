import unittest
from unittest.mock import patch
from api_bigquery_test.bigquery import run_bigquery_query


class TestRunBigqueryQuery(unittest.TestCase):

    @patch('google.cloud.bigquery.Client')
    def test_run_bigquery_query(self, mock_client):
        """
        Unit test for the run_bigquery_query function with mock data.

        This test mocks the BigQuery client to return predefined data
        and verifies the function's behavior.
        """

        # Mock data for the query result
        mock_data = [
            {'ID': 1},
            {'ID': 2},
        ]

        # Mock the query method to return the mock data
        mock_query = mock_client.return_value.query
        mock_query.return_value.result.return_value = mock_data

        # Set project ID, dataset ID, and table ID for the test
        project_id = "your-project-id"
        dataset_id = "your-dataset-id"
        table_id = "your-table-id"

        # Run the function with test data
        results = run_bigquery_query(project_id, dataset_id, table_id)

        # Assertions
        # Verify the number of rows returned
        self.assertEqual(len(results), 2)

        # Verify the content of the first row
        self.assertEqual(results[0]['ID'], 1)


if __name__ == '__main__':
    unittest.main()
