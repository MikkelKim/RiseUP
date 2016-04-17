import StringIO
import unittest2 as unittest

import mock
from scraper import get_keys, get_twitter_api, read_from_filestream


class TestScrapper(unittest.TestCase):

    @mock.patch('scraper.read_from_filestream')
    def test_get_keys(self, mock_read_from_filestream):
        """Fetched keys should contain values from the input."""
        test_input = 'a=1\nb=2\nc=3\nd=4'
        expected = { str(num) for num in range(1,5) }
        mock_read_from_filestream.return_value  = test_input
        result = get_keys()
        self.assertEqual(set(result.values()), expected)

    def test_read_from_filestream(self):
        """Read from StringIO."""
        test_key_file = 'a=1\nb=2\nc=3\nd=4'
        key_file = StringIO.StringIO()
        key_file.write(test_key_file)
        key_file.seek(0)
        result = read_from_filestream(key_file)
        self.assertEqual(result, test_key_file)
    
    @mock.patch('scraper.twitter.Api')
    def test_get_twitter_api(self, mock_twitter_api):
        """Make sure twitter.Api is called."""
        self.assertFalse(mock_twitter_api.called)
        get_twitter_api(dict())
        self.assertTrue(mock_twitter_api.called)


if __name__ == '__main__':
    unittest.main()
