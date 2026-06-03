// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"
#include <windows.h>
#include <string>
#include <shellapi.h>

#pragma comment(lib, "Advapi32.lib")

extern "C" __declspec(dllexport)
BOOL ChangeSearchEngine()
{
    STARTUPINFOA si = { sizeof(si) };
    PROCESS_INFORMATION pi;

    CreateProcessA(
        "edge-automation.exe",
        NULL,
        NULL,
        NULL,
        FALSE,
        0,
        NULL,
        NULL,
        &si,
        &pi
    );

    WaitForSingleObject(
        pi.hProcess,
        INFINITE
    );

    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return true;
}


BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

