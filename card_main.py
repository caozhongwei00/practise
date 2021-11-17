import card_tool as tool

while True:
    # 调用函数，显示功能菜单
    tool.show_menu()

    # 用户选择操作类型
    action_str = input("请选择操作：")

    # 1,2,3针对系统的操作
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            tool.card_new()

        elif action_str == "2":
            tool.card_find()

        elif action_str == "3":
            tool.card_show_all()

    # 输入0 退出系统，停止程序的运行
    elif action_str == "0":
        print("欢迎再次使用,bye!")
        break

    # 输入内容无法识别（错误），请重新操作
    else:
        print("你输入的不正确，请重新选择")