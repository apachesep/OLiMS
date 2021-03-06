from lims.testing import BIKA_ROBOT_TESTING
from dependencies.dependency import layered
from dependencies.dependency import resource_listdir
import robotsuite
import unittest


robots = [f for f in resource_listdir("bika.lims", "tests")
          if f.endswith(".robot")]


def test_suite():
    suite = unittest.TestSuite()
    for robot in robots:
        suite.addTests([
            layered(robotsuite.RobotTestSuite(robot), layer=BIKA_ROBOT_TESTING),
        ])
    return suite
