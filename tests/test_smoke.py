"""
Smoke tests for environment validation.
These tests verify that core dependencies are installed and functional.
"""

def test_core_imports():
    """Verify that essential ML packages can be imported."""
    import numpy as np
    import pandas as pd
    import sklearn
    import pytest
    
    # If we reach here, all imports succeeded
    assert True


def test_numpy_basic_operations():
    """Verify NumPy performs basic operations correctly."""
    import numpy as np
    
    # Create array and test operations
    arr = np.array([1, 2, 3, 4, 5])
    
    assert arr.mean() == 3.0
    assert arr.sum() == 15
    assert len(arr) == 5


def test_pandas_dataframe_creation():
    """Verify Pandas can create and manipulate DataFrames."""
    import pandas as pd
    
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    
    assert df.shape == (3, 2)
    assert list(df.columns) == ['A', 'B']


def test_sklearn_model_import():
    """Verify scikit-learn models can be imported."""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    
    # Instantiate models to confirm they work
    rf = RandomForestClassifier(random_state=42)
    lr = LogisticRegression()
    
    assert rf is not None
    assert lr is not None
