from import_defaults import *
from class_block import *
from class_colors import Colors


class BlockFactory:
    # creates the tetromine after it's been randomly chosen
    options = [I_Block, O_Block, Z_Block, S_Block, J_Block, L_Block, T_Block]

    @staticmethod
    def create(blockType=None):
        if (blockType is None):
            blockType = random.randrange(0, len(BlockFactory.options))

        return BlockFactory.options[blockType]()
