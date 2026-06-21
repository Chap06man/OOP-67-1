class Streamer:    
  def live(self):       
    return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
  def earn(self):       
    return "Заработал 500 донатов за 2 часа"

class TikToker:    
  def live(self):        
   return "Снимаю трендовый тикток под песню месяца!"
  
  def viral(self):        
      return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:    
  def live(self):        
    return "Я... я свечусь в темноте... это мой вайб..."
    
  def superpower(self):       
    return "Летаю и стреляю лазерами из глаза"

class GlowStreamer(Streamer,Mutant):
  def ultimate_content(self):
    return f'{self.earn()} и при этом {self.superpower()}'

  
class ViralCyborg(TikToker,Mutant):
  def ultimate_content(self):
    return f'{self.live()} и потом {self.superpower()}'

class DonateMage(Streamer,TikToker):
  def ultimate_content(self):
    return f'{self.earn()} потому что {self.viral()}'

glow = GlowStreamer()
cyborg = ViralCyborg()
donate =  DonateMage()

print('1.Вызов метода MRO')
print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())

print('2.Метод вызов live')
print(glow.live())
print(cyborg.live())
print(donate.live())

print('3.Комбинирование ')
print(f'1.GlowStreamer: {glow.ultimate_content()}')
print(f'2.ViralCyborg: {cyborg.ultimate_content()}')
print(f'3.DonateMage: {donate.ultimate_content()}')