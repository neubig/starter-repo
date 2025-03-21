from pathlib import Path
import pandas as pd
import pytest

from starter_repo.plot_data import create_plot, read_csv_data


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """Creates and returns a sample CSV file for testing."""
    file_path = tmp_path / "test.csv"
    df = pd.DataFrame({"x": range(1, 6), "y": [2 * i for i in range(1, 6)]})
    df.to_csv(file_path, index=False)
    return file_path


def test_read_csv_data(sample_csv: Path) -> None:
    """Tests reading data from a CSV file."""
    x_data, y_data = read_csv_data(sample_csv, "x", "y")
    assert x_data == [1, 2, 3, 4, 5]
    assert y_data == [2, 4, 6, 8, 10]


def test_create_plot() -> None:
    """Tests plot creation and verifies labels and title."""
    x_data, y_data = [1, 2, 3], [2, 4, 6]
    fig = create_plot(x_data, y_data, "X", "Y", "Test Plot")
    
    assert fig is not None
    ax = fig.axes[0]
    
    assert ax.get_xlabel() == "X"
    assert ax.get_ylabel() == "Y"
    assert ax.get_title() == "Test Plot"
