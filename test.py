from charm.toolbox.pairinggroup import PairingGroup
from PEKS import PEKSClient, PEKSServer

KEYWORD1 = "apple"
KEYWORD2 = "banana"


def main():
   group = PairingGroup('SS512')

   pClient = PEKSClient(group)
   pubKey = pClient.KeyGen()

   pServer = PEKSServer(group, pubKey)

   p = pClient.PEKS(KEYWORD1)
   t1 = pClient.Trapdoor(KEYWORD1)
   t2 = pClient.Trapdoor(KEYWORD2)

   assert pServer.Test(p, t1)
   assert not pServer.Test(p, t2)


if __name__ == '__main__':
   main()
