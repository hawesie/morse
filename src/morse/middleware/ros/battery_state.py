import roslib; roslib.load_manifest('scitos_msgs')
from scitos_msgs.msg import BatteryState
from morse.middleware.ros import ROSPublisher

class BatteryStatePublisher(ROSPublisher):
    """ Publish the charge of the battery sensor. """
    ros_class = BatteryState

    def default(self, ci='unused'):
        msg = BatteryState()

        msg.header = self.get_ros_header()

        msg.lifePercent = int(self.data['charge'])
        # battery life time is unknown, therefore -1
        msg.lifeTime    = -1
        msg.charging    = self.data['charging']
        msg.powerSupplyPresent = self.data['power_supply']

        self.publish(msg)
