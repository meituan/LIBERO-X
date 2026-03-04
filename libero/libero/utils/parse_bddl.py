def parse_bddl_file(file_path):
    """
    解析BDDL文件并返回结构化字典
    
    参数:
        file_path: BDDL文件路径
        
    返回:
        包含解析后数据的字典，结构如下:
        {
            'problem': str,
            'domain': str,
            'language': str,
            'regions': dict,
            'fixtures': dict,  # 类型到数量的映射，如 {"table": 1}
            'objects': dict,   # 类型到数量的映射，如 {"akita_black_bowl": 2}
            'obj_of_interest': list,
            'init': list,
            'goal': list
        }
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 预处理：移除注释和多余空格
    content = '\n'.join(line.split(';')[0].strip() for line in content.split('\n') if line.strip())
    
    # 解析函数
    def _parse(tokens):
        if not tokens: return None
        token = tokens.pop(0)
        if token == '(':
            lst = []
            while tokens[0] != ')':
                lst.append(_parse(tokens))
            tokens.pop(0)
            return lst
        elif token == ')':
            raise ValueError("Unexpected ')'")
        else:
            try: return float(token)
            except: return token
    
    # 词法分析
    tokens = content.replace('(', ' ( ').replace(')', ' ) ').split()
    
    # 语法分析
    parsed = _parse(tokens)
    
    # 转换为结构化字典
    result = {
        'problem': None,
        'domain': None,
        'language': None,
        'regions': {},
        'fixtures': {},
        'objects': {},
        'obj_of_interest': [],
        'init': [],
        'goal': None
    }
    
    # 提取各部分数据
    for item in parsed[2:]:  # 跳过前两个元素(define (problem ...))
        if not item or not isinstance(item, list): continue
        
        key = item[0]
        if key == ':domain':
            result['domain'] = item[1]
        elif key == ':language':
            result['language'] = ' '.join(item[1:])
        elif key == ':regions':
            for region in item[1:]:
                if not isinstance(region, list): continue
                name = region[0]
                data = {}
                for prop in region[1:]:
                    if not isinstance(prop, list): continue
                    if prop[0] == ':target': data['target'] = prop[1]
                    elif prop[0] == ':ranges': data['ranges'] = prop[1]
                    elif prop[0] == ':yaw_rotation': data['yaw_rotation'] = prop[1]
                result['regions'][name] = data
        elif key == ':fixtures':
            # 使用与objects相同的统计方法
            fixtures_list = item[1:]  # 获取所有fixture定义
            i = 0
            while i < len(fixtures_list):
                if fixtures_list[i] == '-':
                    # 当前元素是分隔符，下一个元素是类型
                    fixture_type = fixtures_list[i+1]
                    # 前面的元素都是该类型的实例
                    instance_count = i
                    result['fixtures'][fixture_type] = instance_count
                    # 跳过已处理的部分
                    fixtures_list = fixtures_list[i+2:]
                    i = 0
                else:
                    i += 1
        elif key == ':objects':
            # 使用相同的统计方法
            objects_list = item[1:]  # 获取所有对象定义
            i = 0
            while i < len(objects_list):
                if objects_list[i] == '-':
                    # 当前元素是分隔符，下一个元素是类型
                    object_type = objects_list[i+1]
                    # 前面的元素都是该类型的实例
                    instance_count = i
                    result['objects'][object_type] = instance_count
                    # 跳过已处理的部分
                    objects_list = objects_list[i+2:]
                    i = 0
                else:
                    i += 1
        elif key == ':obj_of_interest':
            result['obj_of_interest'] = [obj for obj in item[1:] if isinstance(obj, str)]
        elif key == ':init':
            result['init'] = [init for init in item[1:] if isinstance(init, list)]
        elif key == ':goal':
            result['goal'] = item[1]
    
    # 设置problem名称
    if len(parsed) > 1 and isinstance(parsed[1], list) and parsed[1][0] == 'problem':
        result['problem'] = parsed[1][1]
    
    return result


# 使用示例
if __name__ == "__main__":
    structured_data = parse_bddl_file('/Users/gdwang/projects/robosuites_color/libero_extension/libero/libero/bddl_files/libero_spatial/pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate.bddl')
    import pdb; pdb.set_trace()
    print(structured_data)
