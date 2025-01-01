from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.HomePageTests import HomePageTest


if __name__ == "__main__":
    test_loader = TestLoader()
    # Add test classes here as list
    test_suite = TestSuite((test_loader.loadTestsFromTestCase(HomePageTest)))
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    # Refer to https://www.lambdatest.com/blog/page-object-model-in-selenium-python/ for more detailed explanation
