# game world list initial
world = [[], [], []] # list of empty object, empty list

# 객체를 게임함수에 추가하는 함수
def add_object(o, depth):
    world[depth].append(o)

def remove_object(o): 
    for layer in world: # 모든 레이어를 순회하면서 제거
        if o in layer:  # 객체가 해당 레이어에 존재하면 제거
            layer.remove(o)
            return # 제거 후 함수 종료

# 게임 로직
def update():
    for layer in world:
        for o in layer[:]:
            o.update()

# 게임 렌더링
def render():
    for layer in world:
        for o in layer:
            o.draw()

