import string


class Cross:

    def __init__(self, word_number, num_of_dots, dic):
        self.index = word_number
        self.num_of_dots = num_of_dots
        self.dic = dic

    def __repr__(self):
        return "Cross index: %s num_of_dots: %s dic: %s" % (self.index, self.num_of_dots, self.dic)

    def replace_dot(self, other_cross):
        if self.index in other_cross.dic:
            replace_location = other_cross.dic[self.index]
            replaced_value = self.dic[other_cross.index]
            st = other_cross.num_of_dots[int(replaced_value)]
            # self.num_of_dots[int(replace_location)] = st
            self.replace_char(int(replace_location), st)
            print(self)

    def replace_char(self, location, replace_value):
        editable = list(self.num_of_dots)
        editable[location] = replace_value
        self.num_of_dots = ''.join(editable)

    # def try_regex(self, regex_string):
    #     if self.could_fit(self, regex_string):
    #         for i in  range (0,len(regex_string)):
    #            self.replace_char(self,self.index[i],sre_yield.AllStrings(regex_string[i], max_count=5, charset=string.ascii_uppercase))

    def could_fit(self, regex):
        if self.num_of_dots == len(regex):
            return True
        else:
            return False

    def only_dots(self):
        has_only_dots = True
        for i in range(0, len(self.num_of_dots)):
            if self.num_of_dots[i] != '.':
                has_only_dots = False
                return has_only_dots
        return has_only_dots
