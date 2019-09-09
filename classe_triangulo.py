class Triangulo:
		def __init__(self,lado_a,lado_b,lado_c):
			self.a = lado_a
			self.b = lado_b
			self.c = lado_c

		def perimetro(self):
				self.t = self.a + self.b + self.c
				return self.t
		
		def tipo_lado(self):
				if self.a == self.b and self.b == self.c:
						x = 'equilátero'
				elif self.a == self.b or self.b == self.c or self.a == self.c:
						x = 'isóceles'
				else:
						x = 'escaleno'

				return x	
