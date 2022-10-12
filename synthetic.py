import numpy as np

def def_timewindow(time_start, time_end, frequency):
    """
    this function returns a time window starting at t_start, finishing at t_end
    with one point every t_samp year
    """
    mynum = int( (time_end - time_start) / frequency ) 
    twindow = np.linspace(time_start, time_end, num=mynum, endpoint = True, dtype=float)
    return twindow

def cos_ts(times, period, amp, phase): 
    """
    this function returns amp * cos( 2pi*times/period + phase )
    """
    ts = amp * np.cos( 2.*np.pi*times/period + phase )
    return ts
