card_list = [{"name": "小王",
              "work": "前端开发",
              "phone": "16382432257"}]

def show_menu():
    """显示菜单"""
    print("欢迎使用名片管理系统\n  1:新建名片\n  2:查询名片\n  3:显示全部名片")
    print("-"*50)


def card_new():
    """新增名片"""

    print("当前界面：新建名片 ")

    # 输入信息
    name_str = input("请输入姓名： ")
    work_str = input("请输入岗位： ")
    phone_str = input("请输入手机号： ")

    card_dict = {"name": name_str,
                 "work": work_str,
                 "phone": phone_str}

    # 添加到名片列表
    card_list.append(card_dict)

    # 提示成功添加
    print("已成功添加%s的名片" % name_str)

    print(""*50)


def card_find():
    """寻找名片"""

    print("当前界面：查询名片 ")

    # 搜索名片
    find_name = input("请输入需查找的姓名： ")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t工作岗位\t\t电话\t\t")
            print("-"*32)
            print("%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                          card_dict["work"],
                                          card_dict["phone"],))
            # 对找到的名片，进行操作
            edit_card(card_dict)
            break

    else:
        print("找不到%s,请检查姓名是否有误" % find_name)

    print("" * 50)


def card_show_all():
    """显示所有名片"""

    print("当前界面：显示全部名片 ")
    if len(card_list) == 0:
        print("当前名片为空，请添加新名片")

        # 如果名片列表为空，返回调用函数的位置，不会返回任何结果
        return

    # 打印表头
    for list_name in ["姓名", "工作岗位", "电话"]:
        print(list_name, end="\t\t")
    print("")
    print("-"*32)

    for card_show in card_list:
        print("%s\t\t%s\t\t%s\t\t" % (card_show["name"],
                                      card_show["work"],
                                      card_show["phone"],))

    print("-"*50)


def edit_card(find_dict):
    """"""
    edit_id = input("请选择操作："
                    "【1】修改名片；【2】删除名片，【3】返回上级菜单")

    # 修改名片
    if edit_id == "1":
        print("当前子界面：修改名片")

        find_dict["name"] = input_card(find_dict["name"], "新的姓名[enter跳过]: ")
        find_dict["work"] = input_card(find_dict["work"], "新的工作岗位[enter跳过]: ")
        find_dict["phone"] = input_card(find_dict["phone"], "新的手机号[enter跳过]: ")

        print("已成功修改")

    # 删除名片
    elif edit_id == "2":
        print("当前子界面：删除名片")

        card_list.remove(find_dict)
        print("已删除名片")

        print("-" * 50)

def input_card(dict_value, tip_info):
    """格式化修改名片信息
    :param dict_value: 查找到名片的原值
    :param tip_info: 用户输入
    :return: 如果用户输入内容为空，返回原值。如果用户输入内容不为空，返回新值。
    """
    # 提示用户输入信息
    result_str = input(tip_info)

    # 针对用户输入的信息进行判断，如果为空，保留原有值
    if len(result_str) == 0:
        return dict_value

    # 针对用户输入的信息进行判断，如果为不为空，替换原有值
    else:
        return result_str
