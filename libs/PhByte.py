from array import array


class PhByte(object):

    '''
        Convert string to byte array

        @return byte array
    '''
    @staticmethod
    def string_to_byte_array(s):
        return array('B', s)

    '''
        Convert an integer to byte array
        
        @param
            @order: 'big', 'little'
            
        @return byte array
    '''
    @staticmethod
    def integer_to_byte_array(i, order):
        return i.to_bytes(4, byteorder=order, signed=True)

