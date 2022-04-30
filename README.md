<details>
  <summary><h2>Automatic response service using Python and Selenium <img src="https://flagicons.lipis.dev/flags/4x3/us.svg" style="width:1em;"/></h2></summary>
  
  ## Problem
  Automatic response to messages from new users who write to the profile of the Tus Clases platform.
  
  ## How the service works?
  Using Selenium, a GET is requested on the url: https://www.tusclases.com.ar/area-profesores/messaging which asks for user's credentials. Then using web scraping techniques and my personal credentials it can log in. Once inside the account there's a logic that's responsible for reviewing latest messages and verifying if within the chats exists a message with my phone number, in case there is no automatic message it is then sent and in that case it will automatically send an email to my personal email that contains the number of people to whom the automatic message was sent and their respective names.
  
  ## Automation of service execution based on Pipelines (GitHub Actions)
  To ensure that the script gets executed periodically, GitHub Actions is used, which allows to define the pipeline buiding (yml file). This file contains a scheduling to execute the pipeline build (and therefore the deployment) every 4 hours. GitHub Action also allows you to set secrets (which are very useful for managing credentials used in code in a safe way).
 <details>
   <summary><h2>Example of the service functionalities</h2></summary>
   
   
  ### 1. GET requested over https://www.tusclases.com.ar/area-profesores/messaging
  ![main](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/tuclases_inicio.png)
  
  ### 2. https://www.tusclases.com.ar/area-profesores/messaging after log in (notice that there's a message without reply)
  ![before](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/teresa_tus_clases_antes.jpg)
  
  ### 3. Python script sends a personalized automatic message.
  ![after](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/teresa_tus_clases_despues.jpg)
  
  ### 4. Message sent to my personal email.
  ![msgmail](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/mail_tus_clases_teresa.JPG)
  
  </details>
  
  ## About GitHub Actions Pricing
  GitHub offers 2000 free minutes/month of execution (this is when the operating system used in the pipeline is Linux), based on the average execution time for the pipeline building (which is 50 seconds), it is estimated that monthly this service will use:
  
<img src="https://latex.codecogs.com/svg.image?\inline&space;\large&space;{\color{White}&space;\mathbf{Used&space;Mins}&space;=&space;\mathbf{50}s/ex&space;\times&space;\mathbf{6}&space;ex/day&space;\times&space;\mathbf{7}&space;days/week&space;\times&space;\mathbf{4}&space;week/month}" title="https://latex.codecogs.com/svg.image?\inline \large {\color{White} \mathbf{UsedMins} = \mathbf{50}s/ex \times \mathbf{6} ex/day \times \mathbf{7} days/week \times \mathbf{4} week/month}" /><br>
<img src="https://latex.codecogs.com/svg.image?\inline&space;\large&space;{\color{White}&space;\mathbf{UsedMins}&space;=&space;\frac{\mathbf{8400}s/month}{\mathbf{60}&space;s/min}&space;=&space;\mathbf{140}&space;min/month}" title="https://latex.codecogs.com/svg.image?\inline \large {\color{White} \mathbf{UsedMins} = \frac{\mathbf{8400}s/month}{\mathbf{60} s/month} = \mathbf{140} min/month}" /><br>
  
140 monthly minutes of execution is an excellent number to have the service in GitHub Actions always running for free.  

</details>


<details>
  <summary><h2>Servicio de respuesta automatica usando Python y Selenium <img src="https://flagicons.lipis.dev/flags/4x3/es.svg" style="width:1em;"/></h2></summary>
  
  ## Problema
  Respuesta automatica de los mensajes de usuarios nuevos que escriben al perfil de la plataforma Tus Clases.
  
  ## ¿Cómo funciona el servicio?
  Usando Selenium se realiza un GET sobre la url: https://www.tusclases.com.ar/area-profesores/messaging la cual solicita las credenciales del usuario. Luego usando tecnicas de web scraping y mi credenciales personales se puede iniciar sesión. Una vez dentro de la cuenta existe una logica que se encarga de revisar los ultimos mensajes y verificar si dentro de las conversaciones existe un mensajes con mi numero de telefono, en caso de que no exista el mensaje automatico es entonces enviado y en ese caso se envia automaticamente un correo a mi mail personal que contiene la cantidad de personas a las que el mensaje automatico fue enviado y sus respectivos nombres.
  
  ## Automatización de la ejecución del servicio basado en pipelines (GitHub Actions)
  Para asegurar que el script se ejecute periodicamente se uso GitHub Actions el cual permite mediante una definicion de construcción de un pipeline (archivo yml) el cual contiene un scheduling para ejecutar la construcción de pipeline (y por lo tanto el deployment) cada 4 horas. GitHub Action tambien permite establecer secretos (los cuales son muy utiles para el manejo de las credenciales usadas en el codigo).
    
  <details>
    <summary><h2>Ejemplo de las funcionalidades del servicio</h2></summary>
 
  ### 1. GET sobre https://www.tusclases.com.ar/area-profesores/messaging
  ![inicio](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/tuclases_inicio.png)
  
  ### 2. https://www.tusclases.com.ar/area-profesores/messaging despues de iniciar sesión (hay un mensaje sin responder)
  ![antes](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/teresa_tus_clases_antes.jpg)
  
  ### 3. El script de python envia el mensaje automatizado personalizado con el nombre de la persona
  ![despues](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/teresa_tus_clases_despues.jpg)
  
  ### 4. Cuerpo del correo enviado a mi mail personal
  ![mail](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/blob/main/images/mail_tus_clases_teresa.JPG)
    
  </details>
  
  ## Sobre los precios de GitHub Action
  GitHub ofrece 2000 minutos/mes gratis de ejecución (esto si el sistema operativo usado en el pipeline es Linux), basandose en el tiempo de ejecución promedio para la construcción del pipeline (el cual es de 50 segundos), se calcula que este servicio mensualmente usara:
  
<img src="https://latex.codecogs.com/svg.image?\inline&space;\large&space;{\color{White}&space;\mathbf{Minutos&space;Usados}&space;=&space;\mathbf{50}s/ej&space;\times&space;\mathbf{6}&space;ej/dia&space;\times&space;\mathbf{7}&space;dias/sem&space;\times&space;\mathbf{4}&space;sem/mes}" title="https://latex.codecogs.com/svg.image?\inline \large {\color{White} \mathbf{Minutos Usados} = \mathbf{50}s/ej \times \mathbf{6} ej/dia \times \mathbf{7} dias/sem \times \mathbf{4} sem/mes}" /><br>
<img src="https://latex.codecogs.com/svg.image?\inline&space;\large&space;{\color{White}&space;\mathbf{MinutosUsados}&space;=&space;\frac{\mathbf{8400}s/mes}{\mathbf{60}&space;s/min}&space;=&space;\mathbf{140}&space;min/mes}" title="https://latex.codecogs.com/svg.image?\inline \large {\color{White} \mathbf{MinutosUsados} = \frac{\mathbf{8400}s/mes}{\mathbf{60} s/min} = \mathbf{140} min/mes}" /><br>
  
140 minutos mensuales de ejecución es un numero excelente para tener el servicio en GitHub Actions ejecutandose siempre de manera gratuita.
  

</details><br>


[![Tus_Clases_Automatic_MSG](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/actions/workflows/push.yml/badge.svg?event=schedule)](https://github.com/engcarlosperezmolero/tus_clases_automatic_response_scraper/actions/workflows/push.yml)
