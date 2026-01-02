"""
Unit tests for poster_service.py
Tests the delete_cached_poster function to ensure it handles None and empty string poster_url values
"""
import os
import tempfile
import unittest
from services.poster_service import delete_cached_poster


class TestDeleteCachedPoster(unittest.TestCase):
    """Test cases for delete_cached_poster function"""

    def setUp(self):
        """Create a temporary directory for poster cache"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_poster_filename = "test_poster.jpg"
        self.test_poster_path = os.path.join(self.temp_dir, self.test_poster_filename)

    def tearDown(self):
        """Clean up temporary directory"""
        if os.path.exists(self.test_poster_path):
            os.remove(self.test_poster_path)
        os.rmdir(self.temp_dir)

    def test_delete_cached_poster_with_none_poster_url(self):
        """Test that delete_cached_poster handles None poster_url without crashing"""
        file_info = {'poster_url': None, 'filename': 'test.mkv'}
        # This should not raise an AttributeError
        try:
            delete_cached_poster(file_info, self.temp_dir)
        except AttributeError:
            self.fail("delete_cached_poster raised AttributeError with None poster_url")

    def test_delete_cached_poster_with_empty_string_poster_url(self):
        """Test that delete_cached_poster handles empty string poster_url"""
        file_info = {'poster_url': '', 'filename': 'test.mkv'}
        # This should not raise an error
        try:
            delete_cached_poster(file_info, self.temp_dir)
        except Exception as e:
            self.fail(f"delete_cached_poster raised exception with empty string poster_url: {e}")

    def test_delete_cached_poster_with_missing_poster_url_key(self):
        """Test that delete_cached_poster handles missing poster_url key"""
        file_info = {'filename': 'test.mkv'}
        # This should not raise an error
        try:
            delete_cached_poster(file_info, self.temp_dir)
        except Exception as e:
            self.fail(f"delete_cached_poster raised exception with missing poster_url key: {e}")

    def test_delete_cached_poster_with_valid_cached_poster(self):
        """Test that delete_cached_poster successfully deletes a cached poster"""
        # Create a test poster file
        with open(self.test_poster_path, 'w') as f:
            f.write("test poster content")

        file_info = {
            'poster_url': f'/poster/{self.test_poster_filename}',
            'filename': 'test.mkv'
        }

        # Verify poster exists before deletion
        self.assertTrue(os.path.exists(self.test_poster_path))

        # Delete the cached poster
        delete_cached_poster(file_info, self.temp_dir)

        # Verify poster was deleted
        self.assertFalse(os.path.exists(self.test_poster_path))

    def test_delete_cached_poster_with_non_cached_url(self):
        """Test that delete_cached_poster ignores non-cached poster URLs"""
        file_info = {
            'poster_url': 'https://image.tmdb.org/t/p/w500/poster.jpg',
            'filename': 'test.mkv'
        }
        # This should not raise an error and should not delete anything
        try:
            delete_cached_poster(file_info, self.temp_dir)
        except Exception as e:
            self.fail(f"delete_cached_poster raised exception with non-cached URL: {e}")

    def test_delete_cached_poster_with_nonexistent_cached_file(self):
        """Test that delete_cached_poster handles nonexistent cached files gracefully"""
        file_info = {
            'poster_url': '/poster/nonexistent_poster.jpg',
            'filename': 'test.mkv'
        }
        # This should not raise an error
        try:
            delete_cached_poster(file_info, self.temp_dir)
        except Exception as e:
            self.fail(f"delete_cached_poster raised exception with nonexistent cached file: {e}")


if __name__ == '__main__':
    unittest.main()
