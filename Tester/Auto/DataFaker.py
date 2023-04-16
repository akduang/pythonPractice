from faker import Faker

# fake = Faker()

#chinese
fake = Faker(locale='zh_CN')


print(fake.name())

print(fake.address())
#从身份证到个人信息 内容非常丰富，但是信息容易重复

# 去重 set（）
#思路1：生成的数据存在set里自动去重
# 生成包含重复数据的列表
names = [fake.name() for _ in range(100)]

# 使用集合去除重复数据
unique_names = set(names)

# 将集合转换回列表
unique_names = list(unique_names)


#思路2:观察输入的数据是否重复
unique_names = set()
while len(unique_names) < 100:
    name = fake.name()
    if name not in unique_names:
        unique_names.add(name)

# 将集合转换回列表
unique_names = list(unique_names)
