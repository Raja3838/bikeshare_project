import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from sklearn.model_selection import train_test_split

from bikeshare_model.config.core import config
from bikeshare_model.processing.data_manager import load_dataset


@pytest.fixture
def sample_input_data():
    data = load_dataset(file_name = config.app_config.training_data_file)
