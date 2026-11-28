import asyncio
import inspect
import time

import drills


def timed(coro):
    """Run a coroutine and return (result, seconds taken)."""
    start = time.perf_counter()
    result = asyncio.run(coro)
    return result, time.perf_counter() - start


# Drill 1 ---------------------------------------------------------------
def test_run_together_returns_results_in_order():
    result, _ = timed(drills.run_together(0.1, 0.1))
    assert result == ["a done", "b done"]


def test_run_together_overlaps_the_waits():
    _, took = timed(drills.run_together(0.3, 0.3))
    assert took < 0.5, f"took {took:.2f}s: the waits did not overlap (expected about 0.3s)"


# Drill 2 ---------------------------------------------------------------
def test_get_label_returns_the_text_not_a_coroutine():
    result, _ = timed(drills.get_label("x"))
    assert result == "x done"


# Drill 3 ---------------------------------------------------------------
def test_blocky_still_returns_its_text():
    result, _ = timed(drills.blocky("a", 0.01))
    assert result == "a done"


def test_blocky_calls_overlap_when_gathered():
    async def both():
        return await asyncio.gather(drills.blocky("a", 0.3), drills.blocky("b", 0.3))

    _, took = timed(both())
    assert took < 0.5, f"took {took:.2f}s: a blocking call froze the loop (expected about 0.3s)"


# Drill 4 ---------------------------------------------------------------
def test_run_limited_keeps_order():
    result, _ = timed(drills.run_limited([0.05, 0.01, 0.03], 2))
    assert result == ["0 done", "1 done", "2 done"]


def test_run_limited_two_at_a_time_takes_two_waves():
    _, took = timed(drills.run_limited([0.2] * 4, 2))
    assert 0.35 <= took < 0.6, f"took {took:.2f}s (expected about 0.4s: two waves of two)"


def test_run_limited_all_at_once_takes_one_wave():
    _, took = timed(drills.run_limited([0.2] * 4, 4))
    assert took < 0.35, f"took {took:.2f}s (expected about 0.2s)"


# Drill 5 ---------------------------------------------------------------
def test_with_fallback_returns_result_when_fast_enough():
    result, _ = timed(drills.with_fallback(0.05, 0.5))
    assert result == "tts done"


def test_with_fallback_gives_up_when_too_slow():
    result, took = timed(drills.with_fallback(2, 0.1))
    assert result == "fallback"
    assert took < 1, "it should stop waiting at the limit, not wait for the slow call"


# Drill 6 ---------------------------------------------------------------
def test_tokens_is_an_async_generator():
    assert inspect.isasyncgenfunction(drills.tokens)


def test_tokens_yields_each_word_in_order():
    async def collect():
        return [w async for w in drills.tokens("hello from the loop")]

    result, _ = timed(collect())
    assert result == ["hello", "from", "the", "loop"]


# Drill 7 ---------------------------------------------------------------
def test_safe_bump_counts_every_increment():
    async def ten_at_once():
        counter = {"n": 0}
        lock = asyncio.Lock()
        await asyncio.gather(*(drills.safe_bump(counter, lock) for _ in range(10)))
        return counter["n"]

    result, _ = timed(ten_at_once())
    assert result == 10, f"got {result}: increments were lost (expected 10)"


# Drill 8 ---------------------------------------------------------------
def test_run_with_signal_returns_go_after_the_event():
    result, took = timed(drills.run_with_signal(0.2))
    assert result == "go"
    assert 0.15 <= took < 0.5, f"took {took:.2f}s (expected about 0.2s)"


# Drill 9 ---------------------------------------------------------------
def test_pipe_passes_items_in_order():
    result, _ = timed(asyncio.wait_for(drills.pipe([1, 2, 3]), 1))
    assert result == [1, 2, 3]


def test_pipe_handles_an_empty_list():
    result, _ = timed(asyncio.wait_for(drills.pipe([]), 1))
    assert result == []
