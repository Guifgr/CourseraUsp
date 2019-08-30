segundos = int(input("Por favor, entre com o número de segundos que deseja converter:\n"))

dia         = int(segundos/86400);
sobraDia    = int(segundos%86400);

hora        = int(sobraDia/3600);
sobraHora   = int(sobraDia%3600);

minuto      = int(sobraHora/60);
sobraMinuto = int(sobraHora%60);

segundo     = int(sobraMinuto);

print("",dia,"dias,",hora,"horas,",minuto,"minutos e",segundo,"segundos.")