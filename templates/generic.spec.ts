import { ComponentFixture, TestBed, async } from '@angular/core/testing';
import { NO_ERRORS_SCHEMA, DebugElement } from '@angular/core';

describe('INSERT_CLASS', (): void => {
    let component: INSERT_CLASS;
    let fixture: ComponentFixture<INSERT_CLASS>;
    let debugElement: DebugElement;

    // Declare services/service stubs

    beforeEach(async((): void => {
        TestBed.configureTestingModule({
            schemas: [NO_ERRORS_SCHEMA],
            declarations: [ INSERT_CLASS ],
            providers: []
        }).compileComponents();
    }));

    beforeEach((): void => {
        fixture = TestBed.createComponent();
        component = fixture.componentInstance;
        debugElement = fixture.debugElement;

        // Get injected services

        // Mock injected services

        // Mock lifecycle hooks

        fixture.detectChanges();
    });

    it('Should instantiate', (): void => {
        expect(component).toBeTruthy();
    });

});