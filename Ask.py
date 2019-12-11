from numpy import pi, sin, linspace, zeros
import matplotlib.pyplot as plt
from fft_modules import amfi_fasma, mono_fasma

word = [1, 0, 1, 1, 0, 1, 0, 1]                            # Η λέξη που θα χρησιμοποιήσω
data_rate = 500                                            # Ρυθμός μετάδοσης 500bps(bits per second)
Tbit = 1 / data_rate                                       # Περίοδος για το κάθε bit

Ac = 1                                                     # Πλάτος φέροντος
fc = 2000                                                  # Συχνότητα φέροντος
Tc = 1/fc                                                  # Περίοδος φέροντος

B = fc                                                     # Μέγιστη συχνότητα
Nyquist = 2 * B                                            # Συχνότητα Nyquist , διπλάσια της μέγιστης συχνότητας στην περίπτωση μας (2 * 2000)
Fs = 50 * Nyquist                                          # Συχνότητα δειγματοληψίας 50 φορές πάνω της συχνότητας Νyquist
Ts = 1/Fs                                                  # Χρόνος δειγματοληψίας
Tmax = Tbit * len(word)                                    # Συνολικός χρόνος 

t = linspace(0, Tmax, Tmax/Ts)      
samples_per_bit = Tbit / Ts                                # Δείγματα ανά περίοδο

carrier = Ac * sin(2*pi*fc*t)                              # Δημιουργία του φέροντος
message=zeros(int(samples_per_bit * len(word)),dtype=int)  # Πληροφορία

for i in range(0, len(word)):                              # Ελέγχω την λέξη όπου έχει άσσο και δημιουργώ τον 1 στην αντίστοιχη θέση του πίνακα zeros
    if word[i] == 1:
        temp = int(i * samples_per_bit)
        message[int(temp): int(temp+samples_per_bit)] = 1

plt.figure(1)      
plt.plot(t,message)
plt.title("Πληροφορία")
plt.xlabel("<-Χρόνος->")
plt.ylabel("<-Πλάτος->")

plt.figure(2)
plt.subplot(2,1,1)
frequencies, amfipleuro = amfi_fasma(message,t)
plt.plot(frequencies,amfipleuro)
plt.title("Aμφίπλευρο φάσμα")
plt.xlabel("<-Συχνότητα(f)->")
plt.ylabel("<-Πλάτος(A)->")
plt.xlim(-Fs/20,Fs/20)

frequencies , monopleuro = mono_fasma(message,t)
plt.subplot(2,1,2)
plt.plot(frequencies,monopleuro)
plt.title("Moνόπλευρο φάσμα")
plt.xlabel("<-Συχνότητα(f)->")
plt.ylabel("<-Πλάτος(A)->")
plt.xlim(-Fs/20,Fs/20)

plt.figure(3)
frequencies , amfipleuro = amfi_fasma(carrier,t)
plt.subplot(2,1,1)
plt.plot(frequencies, amfipleuro)
plt.title("Αμφίπλευρο φάσμα")
plt.xlim(-fc * 2 , fc * 2)

plt.subplot(2,1,2)
frequencies , monopleuro = mono_fasma(carrier,t)
plt.plot(frequencies, monopleuro)
plt.title("Mονόπλευρο φάσμα")
plt.xlim(0, fc * 2)

ask_signal = message * carrier                                         # Δημιουργία ASK (OOK) διαμορφωμένου σήματος

plt.figure(4)
plt.subplot(3,1,1)
plt.plot(t,message)
plt.title("Πληροφορία")
plt.xlabel("<-Χρόνος->")
plt.ylabel("<-Πλάτος->")

plt.subplot(3,1,2)
plt.plot(t,carrier)
plt.title("Φέρων σήμα")
plt.xlabel("<-Χρόνος->")
plt.ylabel("<-Πλάτος->")

plt.subplot(3,1,3)
plt.plot(t,ask_signal)
plt.title("Διαμορφωμένο σήμα")
plt.xlabel("<-Χρόνος->")
plt.ylabel("<-Πλάτος->")

plt.figure(5)
plt.subplot(2,1,1)
frequencies , amfipleuro = amfi_fasma(ask_signal,t)
plt.plot(frequencies, amfipleuro)
plt.title("Αμφίπλευρο Φάσμα")
plt.xlabel("<-Συχνότητα(f)->")
plt.ylabel("<-Πλάτος(A)->")
plt.xlim(-Fs/30,Fs/30)

plt.subplot(2,1,2)
frequencies , monopleuro = mono_fasma(ask_signal,t)
plt.plot(frequencies, monopleuro)
plt.title("Mονόπλευρο Φάσμα")
plt.xlabel("<-Συχνότητα(f)->")
plt.ylabel("<-Πλάτος(A)->")
plt.xlim(0,Fs/30)

plt.show()