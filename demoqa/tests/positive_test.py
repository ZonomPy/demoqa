from utilities.conftest import set_up
from pages.form_data import FormData


def test_forms_positive(set_up):
    driver = set_up
    fd = FormData(driver)
    fd.positive()
