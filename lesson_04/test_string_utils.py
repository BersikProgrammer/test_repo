import pytest
from string_utils import StringUtils

utils = StringUtils()


class TestStringUtils:
    # Тесты для capitalize
    def test_capitalize_normal_string(self):
        assert utils.capitalize("тест") == "Тест"

    def test_capitalize_numbers(self):
        assert utils.capitalize("123") == "123"

    def test_capitalize_with_spaces(self):
        assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"

    def test_capitalize_empty_string(self):
        assert utils.capitalize("") == ""

    def test_capitalize_single_space(self):
        assert utils.capitalize(" ") == " "

    def test_capitalize_none(self):
        with pytest.raises(TypeError):
            utils.capitalize(None)

    # Тесты для trim
    def test_trim_normal_string(self):
        assert utils.trim("   SkyPro") == "SkyPro"

    def test_trim_numbers_with_spaces(self):
        assert utils.trim("   123") == "123"

    def test_trim_string_with_spaces_inside(self):
        assert utils.trim("   04 апреля 2023") == "04 апреля 2023"

    def test_trim_empty_string(self):
        assert utils.trim("") == ""

    def test_trim_only_spaces(self):
        assert utils.trim("    ") == ""

    def test_trim_single_space(self):
        assert utils.trim(" ") == ""

    def test_trim_none(self):
        with pytest.raises(AttributeError):
            utils.trim(None)

    # Тесты для contains
    def test_contains_normal_string(self):
        assert utils.contains("Тест", "Т") is True

    def test_contains_numbers(self):
        assert utils.contains("123", "2") is True

    def test_contains_with_spaces(self):
        assert utils.contains("04 апреля 2023", "апреля") is True

    def test_contains_empty_string_search(self):
        assert utils.contains("Test", "") is True

    def test_contains_in_empty_string(self):
        assert utils.contains("", "a") is False

    def test_contains_none_string(self):
        with pytest.raises(AttributeError):
            utils.contains(None, "a")

    def test_contains_none_symbol(self):
        with pytest.raises(TypeError):
            utils.contains("test", None)

    # Тесты для delete_symbol
    def test_delete_symbol_normal_string(self):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_numbers(self):
        assert utils.delete_symbol("12345", "3") == "1245"

    def test_delete_symbol_with_spaces(self):
        assert utils.delete_symbol("04 апреля 2023", " ") == "04апреля2023"

    def test_delete_symbol_empty_string(self):
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_none_string(self):
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")

    def test_delete_symbol_none_symbol(self):
        with pytest.raises(TypeError):
            utils.delete_symbol("test", None)

    def test_delete_symbol_special_chars(self):
        assert utils.delete_symbol("test@test.com", "@") == "testtest.com"
