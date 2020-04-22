import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_mem_value(file):
    last_line = ""
    with open(file, "r") as file:
        first_line = file.readline()
        for last_line in file:
            pass
    return float(re.findall(r"[0-9]+.[0-9]+ MiB", last_line)[0].replace(" MiB", ""))

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3), sharex=True)

sns.barplot(x=np.array(["superstring", "built-in string"]), y=np.array([get_mem_value("../profiling/super_string_memory.log"), get_mem_value("../profiling/string_memory.log")]), palette="deep", ax=ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Memory Consumption (in MB)")

sns.barplot(x=np.array(["superstring", "built-in string"]), y=np.array([3.087, 14.703]), palette="deep", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Execution time (in s)")

sns.despine(bottom=True)
plt.tight_layout(h_pad=2)

plt.savefig('comparison.png')
