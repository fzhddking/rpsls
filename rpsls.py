#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���һ��
���ڣ�11.23
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        m=0
    elif name=="ʷ����":
        m=1
    elif name=="ֽ":
        m=2
    elif name=="����":
        m=3
    elif name=="����":
        m=4
    else:
        print("Error: No Correct Name")
    return m


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        n="ʯͷ"
    elif number==1:
        n="ʷ����"
    elif number==2:
        n="��"
    elif number==3:
        n="����"
    elif number==4:
        n="����"
    return n
			# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
			# ��Ҫ���Ƿ��ؽ��

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("����������ѡ��")
    a=name_to_number(choice_name)
    b=random.randint(0,4)
    print("------")
    print("����ѡ��Ϊ:%s"%choice_name)
    print("�������ѡ��Ϊ:%s"%number_to_name(b))
    if b==0:
        if a==1 or a==2:
            print("��Ӯ��")
        elif a==3 or a==4:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    elif b==1:
        if a==3 or a==2:
            print("��Ӯ��")
        elif a==0 or a==4:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    elif b==2:
        if a==3 or a==4:
            print("��Ӯ��")
        elif a==0 or a==1:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    elif b==3:
        if a==0 or a==4:
            print("��Ӯ��")
        elif a==1 or a==2:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
    elif b==4:
        if a==0 or a==1:
            print("��Ӯ��")
        elif a==2 or a==3:
            print("�����Ӯ��")
        else:
            print("���ͼ��������һ����")
# ���"-------- "���зָ�
# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

# ����Ļ����ʾ�����ѡ����������

# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




		# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


