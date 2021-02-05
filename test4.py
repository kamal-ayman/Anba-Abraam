from optparse import *


parser = OptionParser("Hello Friend\n\t use -h to help")
parser.add_option('-n', '--name', dest='NameUse', help='Enter your name', default='oliver')
parser.add_option('-g', '--age', dest='AgeUse', help='Enter your age', default='18')
PGroup = OptionGroup(parser, 'other option', 'more option')
PGroup.add_option('-f', '--file', dest='FileName', help='file name')
PGroup.add_option('-l', '--list', dest='ListFile', help='list file name')
parser.add_option_group(PGroup)
(options, args) = parser.parse_args()


if __name__ == '__main__':

    print(f'your name is {options.NameUse} and your age is {options.AgeUse}')
