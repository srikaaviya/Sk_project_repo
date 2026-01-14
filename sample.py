import time

def main():

    start = time.perf_counter()
    time.sleep(2)  # Simulates a delay
    end = time.perf_counter()

    print(int(start))
    print(int(end))
    print(f"Elapsed time: {end - start} seconds")

if __name__ == "__main__":
    main()