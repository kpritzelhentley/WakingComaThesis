from pylsl import StreamInlet, resolve_stream
import matplotlib.pyplot as plt
import matplotlib.animation as anmt
import time

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
counter = 0

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.xlabel('Time')
plt.ylabel('Micro Volts')
plt.title('EEG Channel 1')

data = []
time = []

print("pull samples...")
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample = inlet.pull_sample()
    counter += 1

    data.append(sample[0][0])
    time.append(counter)

    ax1.clear()
    ax1.plot(time,data)
    plt.pause(0.05)

    print(sample)
plt.show()
