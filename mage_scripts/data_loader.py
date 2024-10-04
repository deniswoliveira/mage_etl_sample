import pandas as pd
import random
from datetime import datetime, timedelta

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Generates sample data to load into the Sales.Orders table.

    Returns:
        DataFrame: A DataFrame containing sample order data.
    """
    # Generate sample data
    num_samples = 10  # Specify the number of sample records you want
    customer_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']  # Sample customer names

    data = {
        'CustomerName': [random.choice(customer_names) for _ in range(num_samples)],
        'OrderDate': [datetime.now() - timedelta(days=random.randint(1, 30)) for _ in range(num_samples)],
        'TotalAmount': [round(random.uniform(20.0, 500.0), 2) for _ in range(num_samples)]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
