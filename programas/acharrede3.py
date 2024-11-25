class Rede:
    def __init__ (self, id, ip):
        self.setId(id)
        self.setIp(ip)

    def setId (self, id):
        self.__id = id

    def setIp (self, ip):
        ipf = ip.replace(",", ".")
        lista_ip = ipf.split(".")

        if len(lista_ip) != 4:
            raise ValueError ("IP invalido")

        for ip in lista_ip:
            if not ip.isdigit():
                raise ValueError ("IP invalido")
            
            numero = int(ip)
            if numero < 0 or numero > 255:
                raise ValueError ("IP invalido")
            
            if ip != str(numero):
                raise ValueError ("IP invalido")
        
        self.__ip = ipf
    
    def getIp (self):
        return self.__ip
    
    def getId (self):
        return self.__id
    
    def ipInteiro (self):
        lista_ip = self.__ip.split(".")
        ip_int = 0
        for i in range(4):
            ip_int = ip_int + int(lista_ip[i]) * 256 ** (3-i)
        return ip_int
    
    def __str__ (self):
        return f"IP - {self.__ip}"
    
class Redes:
    redes = []

    @classmethod
    def inserir (cls, obj):
        id = 0
        for x in cls.redes:
            if x.getId() > id:
                id = x.getId()
        obj.setId(id + 1)
        cls.redes.append(obj)

    @classmethod
    def listar (cls):
        return cls.redes
    
class Mascara:
    def __init__ (self, id, msk):
        self.setId(id)
        self.setMsk(msk)

    def setId(self, id):
        self.__id = id

    def setMsk (self, msk):
        if not msk.isdigit():
            raise ValueError ("Mascara invalida")
        
        numero = int(msk)
        if numero < 0 or numero > 32:
            raise ValueError ("Mascara invalida")
        
        self.__msk = int(msk)

    def getId(self):
        return self.__id

    def getMsk (self):
        return self.__msk
    
    def mskInteiro (self):
        mascara_int = 0
        mascara = self.__msk
        for i in range(4,0,-1):
            if mascara >= 8:
                mascara_int = mascara_int + 255 * 256 ** (i-1)
                mascara = mascara - 8
            else:
                mascara_int = mascara_int + 255 - (2**(8 - mascara) - 1)
                mascara = 0
        return mascara_int
    
    def __str__ (self):
        return f"Mascara - {self.__msk}"
    
class Mascaras:
    mascaras = []

    @classmethod
    def inserir (cls, obj):
        id = 0
        for x in cls.mascaras:
            if x.getId() > id:
                id = x.getId()
        obj.setId(id + 1)
        cls.mascaras.append(obj)

    @classmethod
    def listar (cls):
        return cls.mascaras
    
class UI:
    def menu ():
        print("1 - Inserir redes, 2 - Inserir mascara, 3 - Listar redes, 4 - Listar mascaras, 5 - Conferir, 9 - Fim")
        return int(input("Informe sua opção: "))
    
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.novaRede()
            if op == 2:
                UI.novaMascara()
            if op == 3:
                UI.listarRedes()
            if op == 4:
                UI.listarMascaras()
            if op == 5:
                UI.conferir()

    @classmethod
    def novaRede(cls):
        ip = input("Informe o Ip: ")
        rede = Rede(0,ip)
        Redes.inserir(rede)

    @classmethod
    def novaMascara(cls):
        msk = input("Informe a mascara: ")
        mascara = Mascara(0,msk)
        Mascaras.inserir(mascara)

    @classmethod
    def listarRedes(cls):
        redes = Mascaras.listar()
        if len(redes) == 0:
            print("Nenhuma rede cadastrada")
        else:
            for rede in redes:
                print(rede)

    @classmethod
    def listarMascaras(cls):
        mascaras = Mascaras.listar()
        if len(mascaras) == 0:
            print("Nenhuma mascara cadastrada")
        else:
            for mascara in mascaras:
                print(mascara)
        
    @classmethod
    def conferir (cls):
        mascaras = Mascaras.listar()
        redes = Redes.listar()
        if len(redes) < 2 or len(mascaras) < 1:
            print("Opcao indisponivel")
        else:
            for i, rede in enumerate(redes):
                print(f"{i}: {rede}")
            x = int(input("Informe o numero da 1º rede: "))
            y = int(input("Informe o numero da 2º rede: "))
            for i, mascara in enumerate(mascaras):
                print(f"{i}: {mascara}")
            w = int(input("Informe o numero da mascara: "))

            ip1 = redes[x]
            ip2 = redes[y]
            msk = mascaras[w]

            ip1_int = ip1.ipInteiro()
            ip2_int = ip2.ipInteiro()
            msk_int = msk.mskInteiro()

            ip_rede = ip1_int & msk_int
            broadcast = ip1_int | (~msk_int & 0xFFFFFFFF)

            if ip_rede < ip2_int < broadcast:
                    print("os IPs estao na mesma rede.")
            else:
                print("os IPs nao estao na mesma rede.")

UI.main()