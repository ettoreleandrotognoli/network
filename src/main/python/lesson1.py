from typing import List

class InterfaceListerner():

    def next(self, data):
        raise NotImplementedError()


class Interface(InterfaceListerner): 

    def next(self, data):
        raise NotImplementedError()

    def add_listener(self, listener : InterfaceListerner):
        raise NotImplementedError()

class Layer:
    top_interface = None
    bottom_interface = None

    @classmethod
    def connect_all(cls, *layers : List['Layer']):
        for a, b in zip(layers[:-1], layers[1:]):
            a.bottom_interface.add_listener(b.top_interface)
            b.top_interface.add_listener(a.bottom_interface)

    @classmethod
    def crossover(cls, a : 'Layer', b : 'Layer'):
        a.bottom_interface.add_listener(b.bottom_interface)
        b.bottom_interface.add_listener(a.bottom_interface)


class BaseLayer(Layer):

    up_stream = None
    down_stream = None

    def __init__(self):
        self.up_stream = []
        self.down_stream = []

        layer = self

        class TopInterface(Interface):
            
            def add_listener(self, listener : InterfaceListerner):
                layer.up_stream.append(listener)

            def next(self, data):
                layer.send(data)


        self.top_interface = TopInterface()

        class BottomInterface(Interface):
            
            def add_listener(self, listener : InterfaceListerner):
                layer.down_stream.append(listener)

            def next(self, data):
                layer.receive(data)

        self.bottom_interface = BottomInterface()

    def fire_up_stream(self,data):
        for listener in self.up_stream:
            listener.next(data)

    def fire_down_stream(self,data):
        for listener in self.down_stream:
            listener.next(data)

    def send(self,data):
        raise NotImplementedError()

    def receive(self,data):
        raise NotImplementedError()

class DebugListener(InterfaceListerner):

    def __init__(self, prefix = '>'):
        self.prefix = prefix

    def next(self,data):
        print('{}: {}'.format(self.prefix,str(data)))

class StringLayer(BaseLayer):

    def receive(self,data):
        self.fire_up_stream(data)

    def send(self,data):
        self.fire_down_stream(data)

class ReverseLayer(BaseLayer):

    def receive(self,data):
        self.fire_up_stream(data[::-1])

    def send(self,data):
        self.fire_down_stream(data[::-1])

class CharLayer(BaseLayer):

    buffer = None
    
    def __init__(self):
        super().__init__()
        self.buffer = []

    def receive(self,data):
        if data is None:
            self.fire_up_stream(''.join(self.buffer))
            self.buffer = []
        else:
            self.buffer.append(data)

    def send(self,data):
        for c in data:
            self.fire_down_stream(c)
        self.fire_down_stream(None)

Layer3 = StringLayer
Layer2 = ReverseLayer
Layer1 = CharLayer


if __name__ == '__main__':
    a3 = Layer3()
    a2 = Layer2()
    a1 = Layer1()


    b3 = Layer3()
    b2 = Layer2()
    b1 = Layer1()


    #DEBUG
    a3.bottom_interface.add_listener(DebugListener('A3v'))
    a3.top_interface.add_listener(DebugListener('A3^'))
    a2.bottom_interface.add_listener(DebugListener('A2v'))
    a2.top_interface.add_listener(DebugListener('A2^'))
    a1.bottom_interface.add_listener(DebugListener('A1v'))
    a1.top_interface.add_listener(DebugListener('A1^'))

    b3.bottom_interface.add_listener(DebugListener('B3v'))
    b3.top_interface.add_listener(DebugListener('B3^'))
    b2.bottom_interface.add_listener(DebugListener('B2v'))
    b2.top_interface.add_listener(DebugListener('B2^'))
    b1.bottom_interface.add_listener(DebugListener('B1v'))
    b1.top_interface.add_listener(DebugListener('B1^'))

    Layer.connect_all(a3,a2,a1)
    Layer.connect_all(b3,b2,b1)
    Layer.crossover(a1,b1)


    a3.send("Ninguem cresce sozinho")
    b3.send("Ninguem cresce sozinho")
