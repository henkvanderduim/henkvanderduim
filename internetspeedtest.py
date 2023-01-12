# python programma om de
# internet snelheid te testen
#
# importeren van benodigde library
import speedtest as speedtest

# variabele
st = speedtest.speedtest()
option = int(
    input(
        """Welke snelheid wil je testen:
1. Download snelheid
2. Upload snelheid
3. Ping
Jouw keuze: """
    )
)
if option == 1:
    print(st.download())
elif option == 2:
    print(st.upload())
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print("Voer de juiste keuze in aub")
