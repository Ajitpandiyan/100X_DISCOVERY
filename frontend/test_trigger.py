# Test file to trigger workflow

def test_basic():
    """Basic test to ensure CI pipeline works"""
    assert True

def test_environment():
    """Test that we can import basic requirements"""
    import streamlit as st
    assert st is not None