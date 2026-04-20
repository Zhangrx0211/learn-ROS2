"""  
    需求：编写服务端，接收客户端发送请求，提取其中两个整型数据，相加后将结果响应回客户端。
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建服务端；
            3-2.处理请求数据并响应结果。
        4.调用spin函数,并传入节点对象；
        5.释放资源。

"""

# 1.导包；
import rclpy
from rclpy.node import Node
from base_interfaces_demo.srv import Add

# 3.定义节点类；
class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service_py')

        self.get_logger().info("服务端启动！")
        # ***3-1.创建服务端；           服务接口类型 话题名称  回调函数
        self.srv = self.create_service(Add, 'add_ints', self.add_callback)


    # ***3-2.处理请求数据并响应结果。
    def add_callback(self, request, response):
        
        response.sum = request.num1 + request.num2
        self.get_logger().info('请求数据:(%d,%d),响应结果:%d' % (request.num1, request.num2, response.sum))
        return response


def main():
    # 2.初始化 ROS2 客户端；
    rclpy.init()
    # 4.调用spin函数，并传入节点对象；
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    # 5.释放资源。
    rclpy.shutdown()


if __name__ == '__main__':
    main()