# TODO #2 Integrate into one Python file

class Image():
    def __init__(self, filename):
        with open('20/' + filename) as f:
            self.image = list(map(lambda x: list(x.strip()), f.readlines()))
        self.imageHeight = len(self.image)
        self.imageWidth = len(self.image[0])

    def search(self):
        monster = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
        monsterHeight = len(monster)
        monsterWidth = len(monster[0])
        for x in range(self.imageWidth - monsterWidth + 1):
            for y in range(self.imageHeight - monsterHeight + 1):
                found = True
                for i in range(monsterWidth):
                    for j in range(monsterHeight):
                        if monster[j][i] == '#' and self.image[y+j][x+i] not in ['#', 'O']:
                            found = False
                if found:
                    for i in range(monsterWidth):
                        for j in range(monsterHeight):
                            if monster[j][i] == '#':
                                self.image[y+j][x+i] = 'O'

        return sum(map(lambda line: len(list(filter(lambda x: x == '#', line))), self.image))


print(Image('monster_test.txt').search())

print(Image('image1.txt').search())
print(Image('image2.txt').search())
print(Image('image3.txt').search())
print(Image('image4.txt').search())
print(Image('image5.txt').search())
print(Image('image6.txt').search())
print(Image('image7.txt').search())
print(Image('image8.txt').search())