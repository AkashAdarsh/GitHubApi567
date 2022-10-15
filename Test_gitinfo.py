import unittest
from GitInfo import getGitRepoInfo, getNoOfCommits


class TestGitInfo(unittest.TestCase):
    def test_userId(self):
        self.assertEqual(getGitRepoInfo(112345), "User ID is not valid")

    def test_NoOfCommits(self):
        self.assertEqual(getNoOfCommits("Akashadarsh", "GithubAPI567"), 8)

    def test_gitRepos(self):
        self.assertListEqual(getGitRepoInfo("Akashadarsh"),
                             ["Triangle567", "Testing-triangle-classification", "Guess-a-Number", "hello-world","HW-05_Static-Code-Analysis"])


if __name__ == '__main__':
    unittest.main()
