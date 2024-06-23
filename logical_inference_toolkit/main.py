import csv

from models import LogicalReasoner

if __name__ == '__main__':
    examples = [
        "如果正在下雨，那么草是湿的。草是湿的。因此，并没有下雨。",
        "所有的鸟都会飞。企鹅是鸟。因此，企鹅会飞。",
        "如果太阳升起，那么天是亮的。太阳升起了。因此，天是亮的。",
        "所有的猫都会抓老鼠。小猫是猫。因此，小猫会抓老鼠。",
        "如果火山爆发，那么会有熔岩流出。火山爆发了。因此，有熔岩流出。",
        "所有的哺乳动物都生活在陆地上。鲸鱼是哺乳动物。因此，鲸鱼生活在陆地上。",
        "如果一个数是偶数，那么它能被2整除。8是偶数。因此，8能被2整除。",
        "如果一个数是质数，那么它只有1和它自己两个因数。11是质数。因此，11只有1和它自己两个因数。",
        "如果一个动物是哺乳动物，那么它会哺乳。鲸鱼是哺乳动物。因此，鲸鱼会哺乳。",
        "如果一个动物会飞，那么它有翅膀。狗没有翅膀。因此，狗不会飞。"
    ]

    lr = LogicalReasoner()
    csv_file = 'logical_inference_examples.csv'

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['文本', '判断返回（rationale）', '判断结果（logical）'])

        for idx, text in enumerate(examples, 1):
            result = lr(text=text)
            print(f"Example {idx}: {text}")
            print(f"Result: {result}\n")
            writer.writerow([text, result.rationale, result.logical])
