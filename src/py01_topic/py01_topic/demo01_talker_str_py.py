"""  
    需求:以某个固定频率发送文本“hello world!”,文本后缀编号,每发送一条消息,编号递增1。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建发布方；
            3-2.创建定时器；
            3-3.组织消息并发布。
        4.调用spin函数,并传入节点对象；
        5.释放资源。
"""
# 1.导包；
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


# 3.***定义节点类；
class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher_py')
        self.get_logger().info(f"发布方发布了py")
        
        # 3-1.***创建发布方；
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        # 3-2.创建定时器；
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0 #设置计数器

    # 3-3.组织消息并发布。
    def timer_callback(self):
        msg = String() #msg=String类型
        msg.data = 'Hello World(py): %d' % self.i #msg.date=添加数据

        #***发布消息
        self.publisher_.publish(msg) #msg:被发送的消息。
        self.get_logger().info('发布的消息: "%s"' % msg.data)
        self.i += 1


def main():
    # 2.初始化 ROS2 客户端；
    rclpy.init()
    # 4.调用spin函数，并传入节点对象；
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    # 5.释放资源。
    rclpy.shutdown()


if __name__ == '__main__':
    main()