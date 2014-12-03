def look_at_things(R):
    markers = R.see()
    print "I can see", len(markers), "markers:"
    return len(markers)
