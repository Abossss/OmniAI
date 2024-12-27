from agent.interaction import Interaction
import os


def main():
    # 显式设置知识文件路径
    knowledge_file = os.path.join(os.path.dirname(__file__), 'data', 'knowledge.json')

    # 创建 Interaction 实例并传递文件路径
    agent = Interaction(knowledge_file=knowledge_file)

    print("智能助手已启动，输入 'q' 退出。")
    while True:
        user_input = input("您: ")
        if user_input.lower() == 'q':
            print("智能助手已退出，再见！")
            break
        print(f"助手: {agent.interact(user_input)}")


if __name__ == "__main__":
    main()
