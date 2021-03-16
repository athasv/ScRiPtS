def run_timing():
    truns = 0
    ttime = 0
    while True:
        run = input("Ënter 10 km run time: ")
        if not run:
            break

        truns =+ 1
        ttime =+ float(run)

    aver_run = ttime / truns
    print(f'Average of {ttime}, over {truns} runs')
    
run_timing()
 